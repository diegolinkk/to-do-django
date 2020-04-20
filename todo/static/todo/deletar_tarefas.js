deletar = document.querySelectorAll('.link-deletar');
for (i = 0; i < deletar.length; i ++){
    deletar[i].addEventListener('click', function(event){
        event.preventDefault();

        var choice = confirm("Confirma deletar essa tarefa?");

        if(choice) {
            window.location.href = this.getAttribute('href');
        }


    })
}