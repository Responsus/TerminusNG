$("document").ready(function(){
    $("#add-new-task").click(function(){
        var task_text = $("#new-task-text").val();
        var task_description = $("#new-task-description").val();
        var projeto_id = $("#projeto-id").val();
        $.ajax({
            url:"/projetos/"+projeto_id+"/tarefas",
            type: "POST",
            data:{titulo:task_text,descricao:task_description}
        })
        .done(function(data){
            if(data.status == 0){
                $("#project-tasks").append("<li> \
                    <div class='task-checkbox'> \
                        <input type='checkbox' class='flat-grey list-child'/> \
                    </div> \
                    <div class='task-title'> \
                        <span class='task-title-sp'>"+task_text+"</span> \
                        <div class='pull-right hidden-phone'> \
                            <button class='btn btn-default btn-xs'><i class='fa fa-pencil'></i></button> \
                            <button class='btn btn-default btn-xs'><i class='fa fa-times'></i></button> \
                        </div> \
                    </div> \
                </li>");
            }else{
                alert(data.message);
            }
        })
        .fail(function(data){
            console.log(data);
            alert(data.message);
        })
    })


})
