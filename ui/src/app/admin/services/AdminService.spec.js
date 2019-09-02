describe("Service: AdminService", function() {
  beforeEach(module("bassa"));
  beforeEach(module("app"));

  var AdminService;
  var localHttpBackend;
  var localBassaUrl;

  beforeEach(inject(function (_AdminService_, $injector, BassaUrl) {
    AdminService = _AdminService_;
    localHttpBackend = $injector.get("$httpBackend");
    localBassaUrl = BassaUrl;
  }));

  it("should have AdminService be defined", function () {
    expect(AdminService).toBeDefined();
  });

  it("should start downloads", function() {

    localHttpBackend.expect("GET", localBassaUrl + "/api/download/start")
      .respond(201, { "status": "12345" });

    AdminService.startDownloads().then(function(response) {
      expect(typeof response.data).toBe("object");
      expect(typeof response.data.status).toEqual("string");
      expect(response.data.status).toEqual("12345");
    });

  });

  it("should kill downloads", function() {
    
    localHttpBackend.expect("GET", localBassaUrl + "/api/download/kill")
        .respond(200, { status: "success"});
  
    AdminService.killDownloads().then(function(response) {
      expect(typeof response.data).toBe("object");
      expect(response.data.status).toEqual("sucscess");
    });
    
  });

  it("should emit sign up requests", function() {
    
    localHttpBackend.expect("GET", localBassaUrl + "/api/user/requests")
        .respond(200, { requests: "success"});
  
    AdminService.getSignupRequests().then(function(response) {
      expect(typeof response.data).toBe("object");
      expect(response.data.requests).toEqual("success");
    });

  });

  it("should approve user", function() {
    
    localHttpBackend.expect("POST", localBassaUrl + "/api/user/approve/")
        .respond(200, { status: "success"});
  
    AdminService.approve("John Wick").then(function(response) {
      expect(typeof response.status).toBe("string");
      expect(response.data.status).toEqual("success");
    });
    
  });

  it("should approve user", function() {
    
    localHttpBackend.expect("GET", localBassaUrl + "/api/user/heavy/")
        .respond(200, { requests: "success"});
  
    AdminService.getHeavyUsers().then(function(response) {
      expect(typeof response.data).toBe("object");
      expect(response.data.requests).toEqual("success");
    });

  });

});
