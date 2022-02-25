


window.onload = function () {

    var jobs_nav_list = document.getElementsByClassName('jobs_nav_list');
    var nav_pop_container = document.getElementById('nav_pop_container');
    var nav_pop = document.getElementsByClassName('nav_pop');
    
    for(var i=0; i<jobs_nav_list.length; i++) {

        jobs_nav_list[i].num=i;
        jobs_nav_list[i].onmouseover = function () {
            nav_pop_container.style.display = 'block';
            for(var j=0; j<11; j++){
                nav_pop[j].style.display='none';
        };

        nav_pop[this.num].style.display ='block';

        };
 
        
    };

    nav_pop_container.onmouseleave = function(){
        nav_pop_container.style.display = 'none';
    };



    var jobs_brief = document.getElementById('jobs_brief');

    console.log(jobs_brief.offsetHeight);

    var jobs_detail = document.getElementById('jobs_detail');

    jobs_detail.style.marginTop= -jobs_brief.offsetHeight + 'px';



};

