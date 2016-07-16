(function(){
  'use strict';

  angular.module('app')
        .service('SocketService', [
        '$websocket',
      socketService
  ]);

  function socketService(){
    // Open a WebSocket connection
    var dataStream = $websocket('ws://localhost:6800/data');

    var collection = [];

    dataStream.onMessage(function(message) {
      console.log(message);
      collection.push(JSON.parse(message));
    });

    // var methods = {
    //   collection: collection,
    //   get: function() {
    //     dataStream.send(JSON.stringify({ action: 'get' }));
    //   }
    // };

    return collection;
  }
})();
