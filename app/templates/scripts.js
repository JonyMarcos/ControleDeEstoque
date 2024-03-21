// Funções JavaScript
function gerarRelatorio() {
    fetch('http://localhost:5000/gerar-relatorio')
        .then(response => response.json())
        .then(data => {
            const resultadoRelatorio = document.getElementById("resultado-relatorio");
            resultadoRelatorio.innerHTML = "";
            data.forEach(product => {
                resultadoRelatorio.innerHTML += `<p>ID: ${product.id}, Nome: ${product.name}, Quantidade: ${product.quantity}</p>`;
            });
        })
        .catch(error => console.error('Erro ao gerar relatório:', error));
}

function mostrarAtualizacao() {
    document.getElementById("campos-atualizacao").style.display = "block";
    document.getElementById("campos-cadastro").style.display = "none";
}

function mostrarCadastro() {
    document.getElementById("campos-cadastro").style.display = "block";
    document.getElementById("campos-atualizacao").style.display = "none";
}

function atualizarEstoque() {
    const idProduto = document.getElementById("id-produto-atualizar").value;
    const novaQuantidade = document.getElementById("quantidade-produto").value;

    fetch('http://localhost:5000/atualizar-estoque', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id: idProduto, quantity: novaQuantidade })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById("id-produto-atualizar").value = "";
            document.getElementById("quantidade-produto").value = "";
        })
        .catch(error => console.error('Erro ao atualizar estoque:', error));
}

function cadastrarProduto() {
    const nomeProduto = document.getElementById("nome-novo-produto").value;
    const quantidadeProduto = document.getElementById("quantidade-novo-produto").value;

    fetch('http://localhost:5000/cadastrar-produto', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name: nomeProduto, quantity: quantidadeProduto })
    })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            document.getElementById("nome-novo-produto").value = "";
            document.getElementById("quantidade-novo-produto").value = "";
        })
        .catch(error => console.error('Erro ao cadastrar produto:', error));
}
