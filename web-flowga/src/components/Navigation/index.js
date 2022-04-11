import { NavLink as Link } from 'react-router-dom';

// import Styles
import './navigation.scss';

const Navigation = () => {
    return (
        <nav className='navigation-container'>
            <div className='nav-logo'>Flowga</div>
            <div className='nav-links'>
                <Link to='/'> Home </Link>
                <Link to='/about'> About </Link>
                <Link to='/documentation'> Documentation </Link>
            </div>
        </nav>
    )
}

export default Navigation;