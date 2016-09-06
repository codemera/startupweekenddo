var gulp = require('gulp');
var sass = require('gulp-sass');
var notify = require('gulp-notify');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var livereload = require('gulp-livereload');
var scsslint = require('gulp-scss-lint');
var autoprefixer = require('gulp-autoprefixer');
var exec = require('child_process').exec;

config = {
  sassPath: 'startupweekenddo/static/sass',
  jsPath: 'startupweekenddo/static/js',
  bowerDir: 'startupweekenddo/static/components'
}

gulp.task('styles', function() {
    return gulp.src(config.sassPath + '/**/*.scss')
        .pipe(sass({
          includePaths: [
            config.bowerDir + '/bootstrap-sass/assets/stylesheets',
            config.bowerDir + '/font-awesome/scss',
          ]
        })
        .on('error', notify.onError(function (error) {
          return "Error: " + error.message;
        })))
        .pipe(autoprefixer({
          browsers: ['last 2 versions', '> 5%', 'Firefox ESR']
        }))
        .pipe(gulp.dest('startupweekenddo/static/dist/css/'))
        .pipe(livereload());
});

gulp.task('scss-lint', function() {
  return gulp.src(config.sassPath + '/**/*.scss')
    .pipe(scsslint({
      'config': '.scss-lint.yml',
      'endless': 'true'
    }));
});

// gulp.task('task', function(cb) {
//   exec('node_modules/requirejs/bin/r.js -o build.js', function(err, stdout, stderr) {
//     console.log('command was run')
//     console.log(stdout);
//     console.log(stderr);
//     cb(err);
//   });
// });

// Compile Font Awesome
gulp.task('icons', function() {
  return gulp.src(config.bowerDir + '/font-awesome/fonts/**.**')
        .pipe(gulp.dest('startupweekenddo/static/dist/fonts'));
});

// Watch task

gulp.task('watch',function() {
    livereload.listen();
    gulp.watch(config.sassPath + '/**/*.scss', ['styles', 'scss-lint']);
});

gulp.task('default', ['styles', 'icons']);