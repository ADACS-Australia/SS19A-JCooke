/**
 * Distributed under the MIT License. See LICENSE.txt for more info.
 */

$(document).ready(function () {
    function hide_divs(divs) {
        $.each(divs, function () {
            const detached_div = $(this).detach()
            detached_div.appendTo('#form_store')
        })
    }

    function restore_divs_by_template(template_name) {
        let target_id = null;
        $('.row.field.' + template_name).each(function(){
            target_id = $(this).attr('id').replace('inner-', '')
            const detached_div = $(this).detach();
            detached_div.appendTo($('#' + target_id))
        })
    }

    let elements = [];

    $('[id^="div-id_parameter-"]').each(function () {
        let name = $(this).attr('id');

        if (name !== "div-id_parameter-template") {
            elements.push($(this).children(":first"));
        }
    });

    $('#id_parameter-template').each(function () {
        hide_divs(elements);
        restore_divs_by_template($(this).val().split("_")[0]);

        $(this).change(function () {
            hide_divs(elements);
            restore_divs_by_template($(this).val().split("_")[0])
        })
    })
})
