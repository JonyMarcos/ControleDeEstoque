// Lógica JavaScript para mostrar/esconder campos de atualização e cadastro de produtos
document.addEventListener('DOMContentLoaded', function () {
    document.querySelector('#atualizacao-estoque button').addEventListener('click', function () {
        document.getElementById('campos-atualizacao').style.display = 'block';
    });
    document.querySelector('#cadastro-produtos button').addEventListener('click', function () {
        document.getElementById('campos-cadastro').style.display = 'block';
    });
});
