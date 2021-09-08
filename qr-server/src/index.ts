import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';
import authRouter from './routes/authRouter'
import errorHandler from './middlewares/error';

const PORT = 2000
const URI = "mongodb+srv://rut:tur@cluster0.oukiy.mongodb.net/chartrouse?retryWrites=true&w=majority"
//Environment constants

const app = express();
mongoose.connect(URI, {})
//Inicializations

app.use(cors())
app.use(express.json())
app.use('/users', authRouter)
app.use(errorHandler)
//Middleware

app.listen(PORT, () => console.log(`listening on port: ${PORT}`))
mongoose.connection.once('open', () => console.log('MongoDB properly connected!'))
//States