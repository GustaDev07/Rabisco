import CardProdutos from "./CardFunc";

export default function CardList(props) {
  const { funcionarios } = props;
  return (
    <div className="container my-3">
      <div className="row g-3">
        {funcionarios.map((funcionario, index) => {
          return (
            <div key={index} className="col-12 col-sm-6 col-md-4 col-lg-3">
              <CardProdutos
                firts_name={funcionario.first_name}
                last_name={funcionario.last_name}
                email={funcionario.email}
                avatar={funcionario.avatar}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}