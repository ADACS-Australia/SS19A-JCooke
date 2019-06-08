/**
 * Distributed under the MIT License. See LICENSE.txt for more info.
 */

$(document).ready(function () {
    var new_template = 'New Template'
    var old_template = 'Old Template'
    var old_template_elements = []
    old_template_elements.push($('#div-id_parameter-template_date').children(":first"))
    old_template_elements.push($('#div-id_parameter-old_template_name').children(":first"))
    var new_template_elements = []
    new_template_elements.push($('#div-id_parameter-mary_run_template').children(":first"))
    new_template_elements.push($('#div-id_parameter-mary_run_template_sequence_number').children(":first"))

    $('#id_parameter-template').each(function () {
        var divs = null

        if ($(this).val() === new_template) {
            divs = old_template_elements
        }

        if ($(this).val() === old_template) {
            divs = new_template_elements
        }

        hide_forms(divs);

        function hide_forms(divs) {
            $.each(divs, function () {
                var detached_div = $(this).detach()
                detached_div.appendTo('#form_store')
            })
        }
    })
})
