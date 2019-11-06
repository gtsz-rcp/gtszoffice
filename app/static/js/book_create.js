
const appendPartnerObject = function(obj = {}) {
    return Object.assign({
        id: '',
        order: '',
        artist: '',
        artist_name: ''
    }, obj)
}

const array_move = (arr, old_index, new_index) => {
    while (old_index < 0) {
        old_index += arr.length
    }
    while (new_index < 0) {
        new_index += arr.length
    }

    if (new_index >= arr.lenth) {
        let k = new_index - arr.length + 1;
        while(k--) {
            arr.push(undefined)
        }
    }
    arr.splice(new_index, 0, arr.splice(old_index, 1)[0])
    return arr
}

const bookpartnerTypes = [
    {
        value: 'writer', 
        label: 'Writers/Authors'
    },
    {
        value: 'editor', 
        label: 'Editors'
    },
    {
        value: 'designer', 
        label: 'Designers'
    },
    {
        value: 'artist', 
        label: 'Artists'
    }
]

var app = new Vue({
    el: '#app',
    data: {
        bookpartners: [],
        bookpartnerTypes,
        appendPartner: appendPartnerObject(),
        writer: [
            appendPartnerObject({
                artist: 1, 
                artist_name: 'writer test1'
            }),
            appendPartnerObject({
                artist: 1, 
                artist_name: 'writer test2'
            }),
            appendPartnerObject({
                artist: 1, 
                artist_name: 'writer test3'
            })
        ],
        editor: [
            appendPartnerObject({
                artist: 1, 
                artist_name: 'editor test'
            })
        ],
        designer: [
            appendPartnerObject({
                artist: 1, 
                artist_name: 'designer test'
            })
        ],
        artist: [
            appendPartnerObject({
                artist_name: 1, 
                artist: 'artist test'
            })
        ],
        listArtists: [],
    },
    computed: {
        credits() {
            return {
                writer: this.writer,
                editor: this.editor,
                designer: this.designer,
                artist: this.artist,
            }
        },
        toJSON() {
            let _credits = this.credits
            let credits = {}
            Object.keys(_credits)
                .forEach((type) => {
                    credits[type] = _credits[type].map((item, idx) => {
                        item.order = idx + 1
                        return item
                    })
                })
            return JSON.stringify(_credits)
        }
    },
    methods: {
        typeLabelByValue(value) {
            let row = this.bookpartnerTypes.filter((v) => {
                return v.value == value
            })
            
            return row.length > 0 ? row[0].label : ''
        },
        append() {
            if (this.appendPartner.id == '' || this.appendPartner.type == '') return
            let row = this.appendPartner
            let pushdata = {
                artist: row.id,
                artist_name: this.getArtistRowFromId(row.id).name
            }
            this.credits[row.type].push(pushdata)
            this.appendPartner = appendPartnerObject()
        },
        getArtistRowFromId(id) {
            return _.find(this.listArtists, (n) => {
                return n.id == id
            })
        },
        fetchArtists() {
            let vm = this
            return axios.get('/artists')
                .then((response) => {
                    vm.listArtists = response.data
                })
                .catch((err) => {
                    return []
                })
        },
        deleteArtist(type, idx) {
            if(!this[type]) {
                return
            }
            this[type].splice(idx, 1)
        },
        isBtnLeft(idx) {
            return idx > 0
        },
        isBtnRight(idx, length) {
            return idx < (length - 1)
        },
        moveArtist(direction, type, idx) {
            if(!this[type]) {
                return
            }

            let typeArr = this[type]
            let targetIdx = undefined

            switch (direction) {
                case 'left':
                    targetIdx = idx - 1
                    if(targetIdx < 0) {
                        return false;
                    }
                    break;
                
                case 'right':
                    targetIdx = idx + 1
                    if(targetIdx > typeArr.length) {
                        return false
                    }
                    break
                
                default:
                    return false;
            }
            typeArr = this[type]
                .slice(0,0)
                .concat(array_move(typeArr, idx, targetIdx))

        }
    },
    created() {
        this.fetchArtists()
    }
})