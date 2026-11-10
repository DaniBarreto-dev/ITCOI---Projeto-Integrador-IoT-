const API_URL = "http://127.0.0.1:8000/api/medicoes";

async function carregarMedicoes() {
    try {
        const resposta = await fetch(API_URL);
        const medicoes = await resposta.json();

        if (medicoes.length > 0) {
            // Atualiza o painel com a medição mais recente (primeiro item do array)
            const ultima = medicoes[0];
            document.getElementById("distancia-atual").innerText = `${ultima.distancia} cm`;
            document.getElementById("data-atual").innerText = `Atualizado em: ${ultima.data_hora}`;
        }

        // Preenche a tabela com o histórico
        const corpoTabela = document.getElementById("tabela-corpo");
        corpoTabela.innerHTML = "";

        medicoes.forEach(m => {
            const linha = document.createElement("tr");
            linha.innerHTML = `
                <td>${m.id}</td>
                <td>${m.distancia} cm</td>
                <td>${m.data_hora}</td>
            `;
            corpoTabela.appendChild(linha);
        });
    } catch (erro) {
        console.error("Erro ao buscar medições:", erro);
    }
}

// Atualiza a cada 3 segundos
setInterval(carregarMedicoes, 3000);

// Primeira execução ao carregar a página
carregarMedicoes();