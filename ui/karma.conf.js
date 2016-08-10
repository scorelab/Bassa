'use strict';

module.exports = function(config) {

  config.set({
    autoWatch : false,

    frameworks: ['jasmine'],

    browsers : ['PhantomJS2'],

    reporters: ['spec'],

    plugins : [
        'karma-phantomjs2-launcher',
        'karma-jasmine',
        "karma-spec-reporter"
    ]
  });
};
