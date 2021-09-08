import jwt from 'jsonwebtoken';
import userModel from '../models/user.model';
import { Unauthorized, Internal, Unauthenticated } from '../utils/errors';

export const checkAuth = async (req: any, res: any, next: any) => {
    try {
        const token = req.header('Authorization') ? req.header('Authorization').replace('Bearer ', '') : null;
        const payload = jwt.verify(token, "contraseña") as any
        const user = await userModel.findOne({ _id: payload.id, 'tokens.token': token })
        if (!user) { throw new Unauthenticated }
        req.user = user
        req.token = token
        next();
    }
    catch (err) {
        next(err)
    }
}

export const checkModerator = async (req: any, res: any, next: any) => {
    try {
        if (!req.user) { throw new Unauthenticated }
        if (req.user.moderator) {
            next()
        } else {
            throw new Unauthorized
        }
    } catch (err) {
        next(err)
    }
}
