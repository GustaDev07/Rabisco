export default function CardProdutos(props) {
    return (
        <div className="card">
            <img src={`produtos/${props.nome}.png`} className="card-img-top" alt="..."/>
                <div className="card-body">
                    <h5 className="card-title d-flex align-itens-center justify-content-center">{props.nome}</h5>
                    <p className="card-text text-dark d-flex align-itens-center justify-content-center">{props.descricao}</p>
                    <a href="#" className="btn btn-dark d-flex align-itens-center justify-content-center">R$ {props.preco}</a>
                </div>
                <div className="card-footer">
                    <h5 className="card-text text-dark text-center">
                        {props.quantidade} unidade (s) em estoque
                    </h5>
                </div>
        </div>
    )
}
CardProdutos.defaultProps = {
    nome:'Produto',
    descricao:'Descrição do produto',
    quantidade: 0,
    preco: 0.00
}