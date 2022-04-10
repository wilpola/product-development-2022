import { Link } from 'react-router-dom';
const TodayView = () => {
    return (
        <div className='today-container'>
            <h2>Today</h2>
            <Link to='/workout'> Start workout</Link>
        </div>
    )
}
export default TodayView;