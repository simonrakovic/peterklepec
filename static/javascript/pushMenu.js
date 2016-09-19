/**
 * Created by simon on 11/30/14.
 */
    var menuLeft = document.getElementById( 'cbp-spmenu-s1' ),
        showLeftPush = document.getElementById( 'showLeftPush' ),
        body = document.body;


showLeftPush.onclick = function() {
    classie.toggle( this, 'active' );
    classie.toggle( body, 'cbp-spmenu-push-toright' );
    classie.toggle( menuLeft, 'cbp-spmenu-open' );
    disableOther( 'showLeftPush' );
};


function disableOther( button ) {

    if( button !== 'showLeftPush' ) {
        classie.toggle( showLeftPush, 'disabled' );
    }

}