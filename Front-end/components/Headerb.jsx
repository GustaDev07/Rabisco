import Link from 'next/link'
import styles from '../styles/Headerb.module.css'
export default function Headerb(props) {
    return (
        <nav className="navbar navbar-expand-lg bg-dark" data-bs-theme="dark">
            <div className="container-fluid">
                <img src="logo/logo.png" className={styles.img}/>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                        <li className="nav-item">
                            <Link className="nav-link active" aria-current="page" href="/">Home</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link active" aria-current="page" href="/produtos">Produtos</Link>
                        </li>
                        <li className="nav-item">
                            <Link className="nav-link active" aria-current="page" href="/contato">Contato</Link>
                        </li>
                        <li>
                            {props.title}
                        </li>
            
                    </ul>
                    <form className="d-flex" role="search">
                        <input className="form-control me-2" type="search" placeholder="Pesquisar" aria-label="Search"/>
                            <button className="btn btn-outline-white" type="submit">Buscar</button>
                    </form>
                </div>
            </div>
        </nav>
    )
}