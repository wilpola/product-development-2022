import './card.scss';

const DifficultyCard = (props) => {

    return (
        <div className={`difficulty__card-container ${props.className}`}>
            <img src={require(`../../assets/img/${props.img}`)} />
            <h3>{props.title}</h3>
        </div>
    )
}

export {
    DifficultyCard
}