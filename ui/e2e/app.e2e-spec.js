describe('Login Check ', function () {
it('should display an error if the Login Credentials are incorrect', function () {// Visit the login page
browser.get('http://localhost:3000/');//incorrect username entry and password entry
element(by.id('input_0')).sendKeys('lollipop');
element(by.id('input_1')).sendKeys('lollipop'); //Find the submit button and click it
element(by.css('[class="md-raised md-primary login-button md-button md-ink-ripple"]')).click();//Check whether it has the same url
expect(browser.getCurrentUrl()).toEqual('http://localhost:3000/#!/login');
  });
});
describe('Login Check ', function () {
it('should be able to login with default admin credentials', function () {
browser.get('http://localhost:3000/');//use correct login credentials
 element(by.id('input_0')).sendKeys('rand');
element(by.id('input_1')).sendKeys('pass');//Find the submit button and click it
element(by.css('[class="md-raised md-primary login-button md-button md-ink-ripple"]')).click();//login button
  });
});
describe('Check The UI', function () {it (' should click on the dashboard button', function () {
element(by.css('md-sidenav>a:nth-of-type(1)>div:nth-of-type(2)')).click();// click on the dashboard button
});
it('Should type in a link and click the add download button', function () {
element(by.css('input[ng-model="dlink.link"]')).click().sendKeys('https://www.hdwallpapers.in/walls/apple_mac_os_x_el_capitan-wide.jpg');// click the input bar and type in a sample link
element(by.css('[class="md-fab md-wayrn md-mini md-button md-ink-ripple"]')).click();// click the add button
});
it('should go to the admin tab and start the download', function () {// URL: #!/admin
element(by.css('a:nth-of-type(3)')).click();// clicks on the admin tab
element(by.css('[class="md-raised md-primary md-button md-ink-ripple"]')).click();// clicks on start download button
element(by.css('button:nth-of-type(2)')).click();// kills the download
element(by.css('a:nth-of-type(2)>div:nth-of-type(2)')).click(); // goes to the completed tab// URL: #!/table
element(by.css('md-sidenav>a:nth-of-type(1)')).click(); // goes back to dashboard// URL: #!/dashboard
}); // completes the tests.
});

