
const appendPartnerObject = function(obj = {}) {
    return Object.assign({
        type: '',
        id: '',
        name: ''
    }, obj)
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
                id: 1, 
                name: 'writer test'
            })
        ],
        editor: [
            appendPartnerObject({
                id: 1, 
                name: 'editor test'
            })
        ],
        designer: [
            appendPartnerObject({
                id: 1, 
                name: 'designer test'
            })
        ],
        artist: [
            appendPartnerObject({
                id: 1, 
                name: 'artist test'
            })
        ],
        listArtists: []
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
                id: row.id,
                name: this.getArtistRowFromId(row.id).name
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
            console.log(direction, type, idx)
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

            
        }
    },
    created() {
        this.fetchArtists()
    }
})