/* Set the width of the sidebar to 250px (show it) */
function openNav() {
    document.getElementById("mySidepanel").style.width = "250px";
    document.getElementById("openbtn").style.opacity = "0";
    document.body.style.paddingLeft = "250px";

}
  
/* Set the width of the sidebar to 0 (hide it) */
function closeNav() {
    document.getElementById("mySidepanel").style.width = "0";
    document.getElementById("openbtn").style.opacity = "1";
    document.body.style.paddingLeft = "0px";

}