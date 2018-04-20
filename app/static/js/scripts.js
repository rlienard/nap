$(function()
{
  $("#div_l3").hide();

  if(document.getElementById('is_l3').checked)
  {
    $("#div_l3").show();
    $("#div_l3_tl").hide();
    $("#div_l3_hc").hide();
    $("#div_l2").hide();
  }
});
