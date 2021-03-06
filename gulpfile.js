var gulp = require('gulp');
var sass = require('gulp-sass');
var notify = require('gulp-notify');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var livereload = require('gulp-livereload');
var scsslint = require('gulp-scss-lint');
var autoprefixer = require('gulp-autoprefixer');

config = {
  sassPath: 'static/sass',
  jsPath: 'static/js',
  bowerDir: 'static/components',
  distPath: 'static/dist/'
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
        .pipe(gulp.dest(config.distPath + 'css/'))
        .pipe(livereload());
});

gulp.task('scss-lint', function() {
  return gulp.src(config.sassPath + '/**/*.scss')
    .pipe(scsslint({
      'config': '.scss-lint.yml',
      'endless': 'true'
    }));
});

gulp.task('scripts', function() {
    return gulp.src(config.jsPath + '/**/*.js')
        .pipe(concat('scripts.js'))
        .pipe(gulp.dest(config.distPath + 'js/'))
        .pipe(rename('scripts.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest(config.distPath + 'js/'));
});

// Compile Font Awesome
gulp.task('icons', function() {
  return gulp.src(config.bowerDir + '/font-awesome/fonts/**.**')
        .pipe(gulp.dest(config.distPath + 'fonts/'));
});

// Watch task

gulp.task('watch',function() {
    livereload.listen();
    gulp.watch(config.sassPath + '/**/*.scss', ['styles', 'scss-lint']);
});

gulp.task('default', ['styles', 'scripts', 'icons']);
