// Importamos os componentes necessários
import Titulo from '@/components/Titulo';
import Headerb from '../components/Headerb';
import * as React from 'react';
import PyramidLoader from '@/components/PyramidLoader';

// Definimos o componente funcional 'Contato' como o export padrão.
export default function Contato() {
  const [users, setUsers] = React.useState([]); // Estado para armazenar os usuários

  // Função assíncrona para buscar usuários da API ReqRes
  const fetchUsers = async () => {
    try {
      const res = await fetch('https://reqres.in/api/users/');
      const json = await res.json();
      setUsers(json.data); // Atualiza o estado 'users' com os dados recebidos
    } catch (error) {
      console.error('Erro ao buscar usuários:', error);
    }
  };

  // Hook useEffect para executar a busca de usuários ao montar o componente
  React.useEffect(() => {
    fetchUsers();
  }, []);

  // Renderização do componente
  return (
    <>
      <Headerb />
      <Titulo texto="Nossos Funcionários" />
      <div className="container my-3">
        <div className="row g-5">
          {users.map((user) => (
            <div className="col-12 col-sm-6 col-md-4 col-lg-3" key={user.id}>
              <div className="card">
                <img src={user.avatar} className="card-img-top" alt={`${user.first_name} ${user.last_name}`} />
                <div className="card-body">
                  <h5 className="card-title text-center">{`${user.first_name} ${user.last_name}`}</h5>
                  <a href="#" class="btn btn-dark d-flex align-itens-center justify-content-center ">{`${user.email}`}</a>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </>
  );
}