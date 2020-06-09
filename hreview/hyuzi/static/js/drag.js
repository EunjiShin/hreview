
var dragobject= {
    z: 0, x: 0, y: 0, offsetx : null, offsety : null, targetobj : null, dragapproved : 0,
    initialize:function(){
        document.onmousedown=this.drag
        document.onmouseup=function(){this.dragapproved=0}
    },
    drag:function(e){
        var evtobj=window.event? window.event : e
        this.targetobj=window.event? event.srcElement : e.target
        if ((this.targetobj.className=="drag bang") || (this.targetobj.className=="drag back") || (this.targetobj.className=="drag side")){
            this.dragapproved=1
            if (isNaN(parseInt(this.targetobj.style.left))){this.targetobj.style.left=0}
            if (isNaN(parseInt(this.targetobj.style.top))){this.targetobj.style.top=0}
            this.offsetx=parseInt(this.targetobj.style.left)
            this.offsety=parseInt(this.targetobj.style.top)
            this.x=evtobj.clientX
            this.y=evtobj.clientY
            if (evtobj.preventDefault)
                evtobj.preventDefault()
            document.onmousemove=dragobject.moveit
        }
    },
    moveit:function(e){
        var evtobj=window.event? window.event : e
        if (this.dragapproved==1){
            this.targetobj.style.left=this.offsetx+evtobj.clientX-this.x+"px"
            this.targetobj.style.top=this.offsety+evtobj.clientY-this.y+"px"
            return false
        }
    }
}
dragobject.initialize()
    
// 얼굴형을 선택하는 함수
function selectFace(obj) {       
    switch (obj) {
        case 'circle':
            document.getElementById("result").innerHTML = "<img src='/static/img/circle.png' id='circle' width='300px'>";
                break;
        case 'rectangle': 
            document.getElementById("result").innerHTML = "<img src='/static/img/rectangle.png' id='rectangle' width='300px'>";
                break;
        case 'oval': 
            document.getElementById("result").innerHTML = "<img src='/static/img/oval.png' id='oval' width='300px'>";
                break;
        default: 
            document.getElementById("result").innerHTML = ""; 
            break;
    }
}

// pieces image store
    var black_bang = ["../../static/img/bang1.png", "../../static/img/bang2.png"];
    var black_side = ["../../static/img/bang3.png"];
    var black_back = ["../../static/img/bang4.png"];
    
    var pink_bang =["../../static/img/long1.jpg", "../../static/img/long2.jpg"];
    var pink_side = ["../../static/img/short1.jpg"];
    var pink_back = ["../../static/img/long3.jpg"];
    
    var purple_bang = ["../../static/img/others1.jpg"];
    var purple_side = ["../../static/img/others2.jpg"];
    var purple_back = ["../../static/img/others3.jpg", "../../static/img/others4.jpg"];
    
    var green_bang = ["../../static/img/tiger.png"];
    var green_side = ["../../static/img/rabbit.png"];
    var green_back = ["../../static/img/elephant.png"];
    
// 이미지 띄우는 함수
    function change(color) {
        var imageCode="";
        if(color=="black"){
            for(var i=0; i<black_bang.length; i++) {
                imageCode+="<img class='drag bang' src='";
                imageCode+=black_bang[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<black_side.length; i++) {
                imageCode+="<img class='drag side' src='";
                imageCode+=black_side[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<black_back.length; i++) {
                imageCode+="<img class='drag back' src='";
                imageCode+=black_back[i];
                imageCode+="' width='300px'>";
            }
        }
        else if(color=="pink") {
            for(var i=0; i<pink_bang.length; i++) {
                imageCode+="<img class='drag bang' src='";
                imageCode+=pink_bang[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<pink_side.length; i++) {
                imageCode+="<img class='drag side' src='";
                imageCode+=pink_side[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<pink_back.length; i++) {
                imageCode+="<img class='drag back' src='";
                imageCode+=pink_back[i];
                imageCode+="' width='300px'>";
            }
        }
        else if(color=="purple") {
            for(var i=0; i<purple_bang.length; i++) {
                imageCode+="<img class='drag bang' src='";
                imageCode+=purple_bang[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<purple_side.length; i++) {
                imageCode+="<img class='drag side' src='";
                imageCode+=purple_side[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<purple_back.length; i++) {
                imageCode+="<img class='drag back' src='";
                imageCode+=purple_back[i];
                imageCode+="' width='300px'>";
            }
        }
        else {
            for(var i=0; i<green_bang.length; i++) {
                imageCode+="<img class='drag bang' src='";
                imageCode+=green_bang[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<green_side.length; i++) {
                imageCode+="<img class='drag side' src='";
                imageCode+=green_side[i];
                imageCode+="' width='300px'>";
            }
            for(var i=0; i<green_back.length; i++) {
                imageCode+="<img class='drag back' src='";
                imageCode+=green_back[i];
                imageCode+="' width='300px'>";
            }
        }
        
        document.getElementById("pieces").innerHTML = imageCode;
    }
