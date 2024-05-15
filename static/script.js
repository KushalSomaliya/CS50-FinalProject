document.addEventListener("DOMContentLoaded", function() {
    window.addEventListener("scroll", function() {
        
        var div = document.querySelector('.leftcolumn');
        var computedStyle = window.getComputedStyle(div);
        var marginTop = computedStyle.getPropertyValue('margin-top');
        var newMarginTop = marginTop - "1";
        
        console.log("Margin-top:", marginTop);
        if (marginTop = 0) {
            ;
        }
        else {
            div.style.marginTop = newMarginTop + "px";
        }
    })
})


