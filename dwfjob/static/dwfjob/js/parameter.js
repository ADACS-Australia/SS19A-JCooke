/**
 * Distributed under the MIT License. See LICENSE.txt for more info.
 */

$(document).ready(function () {
    var new_template = 'new_template'
    var old_template = 'old_template'

    var old_template_elements = []
    old_template_elements.push($('#div-id_parameter-template_date').children(":first").addClass('div-id_parameter-template_date'))
    old_template_elements.push($('#div-id_parameter-old_template_name').children(":first").addClass('div-id_parameter-old_template_name'))

    old_template_elements.forEach(function (element) {
        element.addClass(old_template)
    })

    var new_template_elements = []
    new_template_elements.push($('#div-id_parameter-mary_run_template').children(":first").addClass('div-id_parameter-mary_run_template'))
    new_template_elements.push($('#div-id_parameter-mary_run_template_sequence_number').children(":first").addClass('div-id_parameter-mary_run_template_sequence_number'))

    new_template_elements.forEach(function (element) {
        element.addClass(new_template)
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

            restore_divs_by_class($(this).val())
        })

        function restore_divs_by_class(template_name) {
            var class_name = null
            var target_id = null

            $('.' + template_name).each(function () {
                var class_names = $(this).attr('class').split(" ")
                target_id = class_names.slice(-2, -1)[0]
                class_name = "." + target_id + "." + class_names.slice(-1)[0]
                var detached_div = $(class_name).detach()
                detached_div.appendTo($('#' + target_id))
            })
        }

        function hide_divs(divs) {
            $.each(divs, function () {
                var detached_div = $(this).detach()
                detached_div.appendTo('#form_store')
            })
        }
    })
})
