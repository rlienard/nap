$(function()
{
  $("#div_router").hide();
  $("#div_switch").hide();
  $("#div_l2").hide();
  $("#div_l3").hide();

  $('#device_model').change(function()
  {
    var selected_value = $(this).val();
    if(selected_value == 0)
    {
      $("#div_router").hide();
      $("#div_switch").hide();
      $("#div_l2").hide();
      $("#div_l3").hide();
    }
    if(selected_value == 1) //3650
    {
      $("#div_router").hide();
      $("#div_switch").show();
      $("#div_l2").show();
      $("#div_switch_is_l3").show();
      $("#div_switch_members_in_stack").show();
    }
    if(selected_value == 2) //3560CX
    {
      $("#div_router").hide();
      $("#div_switch").show();
      $("#div_l2").show();
      $("#div_switch_is_l3").show();
      $("#div_switch_members_in_stack").hide();
    }
    if(selected_value == 3) //3560CG
    {
      $("#div_router").hide();
      $("#div_switch").show();
      $("#div_l2").show();
      $("#div_switch_members_in_stack").hide();
      $("#div_switch_is_l3").hide();
    }
    if(selected_value == 4) //ISR3
    {
      $("#div_router").show();
      $("#div_switch").hide();
      $("#div_l2").hide();
      $("#div_l3").hide();
    }
  });

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
