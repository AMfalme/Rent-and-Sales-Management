$(
    function (params) {
        
        $('.nav-link').click(
            (params) =>{
                console.log($(this))
                var clickedLink = $(this).next()
                console.log(clickedLink)
                clickedLink.css( "background-color", "red" );
                var i;
                
            } 
            )
            $('#navbar-button').click(
                ()=>{
                    console.log('clicked')
                    
                    setTimeout(
                        function() {
                            $('#side-bar').toggleClass('clicked')
                            $('.resize-sm').toggleClass('nav-open')
                        }, 100)}
            )
                }
    
);
