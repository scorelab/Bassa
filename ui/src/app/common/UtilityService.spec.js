describe('Service: UtilityService', function() {
  'use strict';
  beforeEach(module('app'));

  var UtilityService;

  beforeEach(inject(function (_UtilityService_) {
    UtilityService = _UtilityService_;
  }));

  it('Should have UtilityService be defined', function () {
    expect(UtilityService).toBeDefined();
  });

  describe('formatBytes', function() {
    it("Gives '0 Byte' when bytes equals 0", function() {
      expect(UtilityService.formatBytes(0)).toEqual('0 Byte');
    });

    it("Gives '1.045 KB' when bytes equals 1045", function() {
      expect(UtilityService.formatBytes(1045)).toEqual('1.045 KB');
    });

    it("Gives '2 MB' when bytes equals 2000000", function() {
      expect(UtilityService.formatBytes(2000000)).toEqual('2 MB');
    });

    it("Rounds off to 3 decimal places and gives '20.003 MB' when bytes equals 20003124", function() {
      expect(UtilityService.formatBytes(20003124)).toEqual('20.003 MB');
    });

  });

});
