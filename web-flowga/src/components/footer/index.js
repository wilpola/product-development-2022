import './footer.scss';
import AMKLogo from '../../assets/img/turku_amk_eng_logo.png';
const Footer = () => {

    return (

        <footer className='footer-container'>
            <div className='footer-upper'>
                <div className='footer-logo'>
                    <h2> Meddler Labs</h2>
                    <img src={AMKLogo} />
                </div>
            </div>
            <div className='footer-lower'>
                <h5>	&copy; 2022 Meddler Labs </h5>
            </div>
        </footer>
    )
}
export default Footer;