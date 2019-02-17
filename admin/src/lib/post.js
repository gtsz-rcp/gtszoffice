import moment from 'moment'

function postManipulate (item) {
  item.is_feature_str = item.is_feature === true ? 'Y' : 'N'
  item.is_list_str = item.is_list_str === true ? 'Y' : 'N'
  item.createtime_str = moment(item.createtime).format('YYYY-MM-DD')
  return item
}

export { postManipulate }
