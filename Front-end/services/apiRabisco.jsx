import axios from 'axios'

// Cria uma instância do axios com uma configuração básica
const api = axios.create({ baseURL: 'http://127.0.0.1:5000' })

// Função assíncrona para obter produtos do endpoint /produto
export async function getProdutos() {
    try {
        // Realiza uma requisição GET ao endpoint /produto usando a instância do axios
        const response = await api.get('/produto')
        // Retorna os dados da resposta da requisição
        return response.data
    } catch (error) {
        // Em caso de erro na requisição, exibe uma mensagem de erro no console
        console.error(`Erro ao buscar produtos: ${error.message}`)
    }
}
