$(document).ready(function(){
  $('.hidden').hide();


  $('.lesson-title').click(function(){
    arrownDownPath = '/static/lessons/images/arrowDown.png';
    arrownRightPath = '/static/lessons/images/arrowRight.png';

    content = $(this).parent().find('.lesson-content-container');
    $content = $(content);
    isDisplayed = $content.hasClass('displayed');
    arrow = $(this).find('.arrow');
    $arrow = $(arrow);

    if(isDisplayed) {
      $content.removeClass('displayed');
      $content.addClass('hidden');
      $content.hide();
      $arrow.attr('src', arrownRightPath);
      $arrow.removeClass('arrow-down');
      $arrow.addClass('arrow-right');
    }
    else {
      $content.removeClass('hidden');
      $content.addClass('displayed');
      $content.show();
      $arrow.attr('src', arrownDownPath);
      $arrow.removeClass('arrow-right');
      $arrow.addClass('arrow-down');
    }

  });

  $('#highlight-levels').change(function(){
    if ($(this).is(':checked')) {
      $('.assignment').addClass("level-highlighted");
    }
    else {
      $('.assignment').removeClass("level-highlighted");
    }
  });
});
