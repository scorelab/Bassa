describe('Controller: Admin controller', function() {
  'use strict';
  beforeEach(module('bassa'))
  beforeEach(module('app'));

  var scope, AdminCtrl, BassaUrl;

  var fakeHttpPromise = function () {
    return {
      then: function () {
        return true;
      }
    };
  };

  beforeEach(inject(function($controller, $rootScope) {

    scope = $rootScope.$new();
    AdminCtrl = $controller('AdminCtrl', {
       '$scope': scope
    });

  }));

  it('should have AdminCtrl defined', function() {
      expect(AdminCtrl).toBeDefined();
  });

  it('start should call AdminService.startDownloads()', inject(function (AdminService) {

    spyOn(AdminService, 'startDownloads').and.callFake(fakeHttpPromise);
  
    scope.start();
  
    expect(AdminService.startDownloads).toHaveBeenCalled();
  
  }));

  it('kill should call AdminService.killDownloads()', inject(function (AdminService) {

    spyOn(AdminService, 'killDownloads').and.callFake(fakeHttpPromise);
  
    scope.kill();
  
    expect(AdminService.killDownloads).toHaveBeenCalled();
  
  }));

  it('approve should call AdminService.approve()', inject(function (AdminService) {

    spyOn(AdminService, 'approve').and.callFake(fakeHttpPromise);
  

    var user = {
        user_name: 'BassaUser',
        email: 'user@bassa.com',
        password: 'bassapass'
    }

    scope.approve(user);
  
    expect(AdminService.approve).toHaveBeenCalled();
  
  }));

  it('getRequests should call AdminService.getSignupRequests()', inject(function (AdminService) {

    spyOn(AdminService, 'getSignupRequests').and.callFake(fakeHttpPromise);
  
    AdminCtrl.getRequests();
  
    expect(AdminService.getSignupRequests).toHaveBeenCalled();
  
  }));

  it('getHeavyUsers should call AdminService.getHeavyUsers()', inject(function (AdminService) {
    
    spyOn(AdminService, 'getHeavyUsers').and.callFake(fakeHttpPromise);
  
    AdminCtrl.getHeavyUsers();
  
    expect(AdminService.getHeavyUsers).toHaveBeenCalled();
  
  }));
});
