/**
 * Distributed under the MIT License. See LICENSE.txt for more info.
 */

$(document).ready(function () {
  var new_template = 'New Template'
  var old_template = 'Old Template'

  var old_template_elements = []
  old_template_elements.push($('#div-id_parameter-template_date').children(":first").addClass('div-id_parameter-template_date'))
  old_template_elements.push($('#div-id_parameter-old_template_name').children(":first").addClass('div-id_parameter-old_template_name'))

  old_template_elements.forEach(function (element) {
    element.addClass('old_template')
  })

  var new_template_elements = []
  new_template_elements.push($('#div-id_parameter-mary_run_template').children(":first").addClass('div-id_parameter-mary_run_template'))
  new_template_elements.push($('#div-id_parameter-mary_run_template_sequence_number').children(":first").addClass('div-id_parameter-mary_run_template_sequence_number'))

  new_template_elements.forEach(function (element) {
    element.addClass('new_template')
  })

  $('#id_parameter-template').each(function () {
    var divs = []

    if ($(this).val() === new_template) {
      divs = old_template_elements
    }

    if ($(this).val() === old_template) {
      divs = new_template_elements
    }

    hide_divs(divs)

    $(this).change(function () {
      divs = old_template_elements.concat(new_template_elements)
      hide_divs(divs)
      // console.log(old_template_elements[0].attr('class'))

      var detached_divs = null

      if ($(this).val() === old_template) {
        detached_divs = $('#form_store > ' + '.old_template').detach()
      }

      if ($(this).val() === new_template) {
        detached_divs = $('#form_store > ' + '.new_template').detach()
      }

      restore_divs(detached_divs)
    })


    function restore_divs(detached_divs) {
      var class_name = null
      var target_id = null

      for (var i = 0; i < detached_divs.length; i++) {
        target_id = detached_divs[i].className.split(" ").slice(-2, -1)[0]
        class_name = "." + target_id + "." + detached_divs[i].className.split(" ").slice(-1)[0]
        console.log(target_id)
        console.log($(class_name))
        $(class_name)[0].appendTo('#' + target_id)
      }
    }


    function hide_divs(divs) {
      $.each(divs, function () {
        var detached_div = $(this).detach()
        detached_div.appendTo('#form_store')
      })
    }
  })
})
