describe('Service: TableService', function() {
  'use strict';
  beforeEach(module("bassa"));
  beforeEach(module("app"));

  var TableService;
  var localBassaUrl;
  var localHttpBackend;

  beforeEach(inject(function (_TableService_, $injector, BassaUrl) {
    TableService = _TableService_;
    localHttpBackend = $injector.get("$httpBackend");
    localBassaUrl = BassaUrl;
  }));

  it('Should have TableService be defined', function () {
    expect(TableService).toBeDefined();
  });

  describe('getCompletedDownloads', function() {
    
    it('Should return a promise [object]', function() {
      
      localHttpBackend.expect("GET", localBassaUrl + "api/downloads/1")
      .respond(201, { "status": "12345" });

      expect(typeof TableService.getCompletedDownloads()).toEqual('object');
    });

  });
});
