/**
 * Distributed under the MIT License. See LICENSE.txt for more info.
 */

$(document).ready(function () {

    $('[id^="link-image-"]').click(function () {
        let name = $(this).attr('id');
        hide_show_images(name.replace('link-image-', ''))
    });

    $('[id^="view-image-"]').click(function () {
        let name = $(this).attr('id');
        hide_show_images(name.replace('view-image-', ''))
    });

    function hide_show_images(id_val) {
        $('[id^="div-image-"]').each(function() {
            let name = $(this).attr('id');
            if (name.endsWith(id_val)) {
                $(this).removeClass('d-none')
            } else {
                $(this).addClass('d-none')
            }
        })
    }
})
