import mongoose from 'mongoose';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        unique: true,
        required: [true, "Debe indicar un nombre de usuario"]
    },
    pass: {
        type: String,
        unique: true,
        required: [true, "Debe indicar una contraseña"]
    },
    moderator: {
        type: Boolean,
        required: [true, "Debe indicar una jerarquia"],
        default: false,
    },
    tokens: [{
        token: {
            type: String,
            required: [true, "Debe indicar un token"],
        }
    }]
})

userSchema.pre('save', async function (next) {
    if (this.isModified('pass')) {
        this.pass = await bcrypt.hash(this.pass, 8);
    }
    next();
})

userSchema.methods.generateAuthToken = async function () {
    const token = jwt.sign({ id: this._id }, "contraseña")
    this.tokens = this.tokens.concat({ token })
    await this.save()
    return token
}

userSchema.statics.findByCredentials = async (name, pass) => {
    const user = await userModel.findOne({ name }) as any
    if (!user) {
        throw new Error('Usuario o Contraseña incorrectos')
    }
    const isPasswordMatch = await bcrypt.compare(pass, user.pass)
    if (!isPasswordMatch) {
        throw new Error('Usuario o Contraseña incorrectos')
    }
    return user
}

const userModel = mongoose.model('User', userSchema, 'Users');

export default userModel;