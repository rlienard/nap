$(function()
{
  $("#div_l3").hide();

  $('#is_l3').change(function()
  {
    if($(this).prop("checked"))
    {
      $('#div_l2').hide("slow");
      $('#div_l3').show("slow");
      $('#div_l3_hc').hide("slow");
      $('#div_l3_tl').hide("slow");
    }

    else
    {
      $('#div_l2').show("slow");
      $('#div_l3').hide("slow");
    }
  });

  $('#has_tl').change(function()
  {
    if($(this).prop("checked") && $('#is_l3').prop("checked"))
    {
      $('#div_l3_tl').show("slow");
    }

    else
    {
      $('#div_l3_tl').hide("slow");
    }
  });

  $('#has_hc').change(function()
  {
    if($(this).prop("checked") && $('#is_l3').prop("checked"))
    {
      $('#div_l3_hc').show("slow");
    }

    else
    {
      $('#div_l3_hc').hide("slow");
    }
  });
});
