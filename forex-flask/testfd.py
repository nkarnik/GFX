from fluent import sender
from fluent import event
sender.setup('hdfs', host='localhost', port=24224)
event.Event('testfd.forex', {
    'pair': 'USDJPY',
    'value': '120.32'
})
