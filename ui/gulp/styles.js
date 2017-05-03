'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');

var paths = gulp.paths;

var $ = require('gulp-load-plugins')();

// gulp.task('styles', function() {
//   return gulp.src(paths.src + 'app/index.scss') // Gets all files ending with .scss in app/scss and children dirs
//     .pipe(sass()) // Passes it through a gulp-sass
//     .pipe(gulp.dest(paths.tmp + '/serve/app/')) // Outputs it in the css folder
//     ;
// })

gulp.task('styles', function () {

  var sassOptions = {
    style: 'expanded',
    'sourcemap=none': true
  };

  var injectFiles = gulp.src([
    paths.src + '/{app,components}/**/*.scss',
    '!' + paths.src + '/app/index.scss',
    '!' + paths.src + '/app/vendor.scss'
  ], { read: false });

  var injectOptions = {
    transform: function(filePath) {
      filePath = filePath.replace(paths.src + '/app/', '');
      filePath = filePath.replace(paths.src + '/components/', '../components/');
      return '@import \'' + filePath + '\';';
    },
    starttag: '// injector',
    endtag: '// endinjector',
    addRootSlash: false
  };

  var indexFilter = $.filter('index.scss');

  return gulp.src([
    paths.src + '/app/index.scss',
    paths.src + '/app/vendor.scss'
  ])
    .pipe(indexFilter)
    .pipe($.inject(injectFiles, injectOptions))
    .pipe(indexFilter.restore())
    .pipe(sass(sassOptions)
      .on('error', function (err) {
        console.error('Error!', err);
      })
    )

  .pipe($.autoprefixer())
    .on('error', function handleError(err) {
      console.error(err.toString());
      this.emit('end');
    })
    .pipe(gulp.dest(paths.tmp + '/serve/app/'));
});
