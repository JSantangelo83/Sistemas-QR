import userModel from '../models/user.model'
import { checkAuth, checkModerator } from '../middlewares/auth'
import { Unauthorized, Internal } from '../utils/errors';

const authRouter = require('express').Router();

authRouter.route('/access/login').post(async (req: any, res: any, next: any) => {
    try {
        const { name, pass } = req.body
        let user = await (userModel as any).findByCredentials(name, pass)
        if (!user) { throw new Unauthorized }
        const token = await user.generateAuthToken()
        res.send({ user, token })
    } catch (err) {
        next(err)
    }
})

// authRouter.route('/testing/createmoderator').post((req, res) => {
//     let moderatorData = {}
//     Object.keys(req.body).map(k => moderatorData[k] = req.body[k])
//     const newModerator = new userModel(moderatorData)
//     newModerator.save(err => res.status(err ? 400 : 200).send(err ? err : 'Moderador creado con exito!'))
// })

authRouter.route('/').get(checkAuth, checkModerator, (req: any, res: any, next: any) => {
    try {
        userModel.find((err, users) => { if (err) { throw new Internal(err.message) } else { res.status(200).json(users) }; })
    } catch (err) { next(err) }
})

authRouter.route('/').post(checkAuth, checkModerator, (req: any, res: any, next: any) => {
    try {
        const newUser = new userModel(req.body)
        newUser.save(err => {
            if (err) { throw new Internal(err.message) } else { res.status(200).send('Usuario creado con exito!') }
        })
    } catch (err) { next(err) }
})

authRouter.route('/:id').delete(checkAuth, checkModerator, (req: any, res: any, next: any) => {
    try {
        userModel.findByIdAndDelete(req.params.id, null, err => {
            if (err) { throw new Internal(err.message) } else { res.status(200).send('Usuario eliminado con exito!') }
        })
    } catch (err) { next(err) }
})

authRouter.route('/:id').get(checkAuth, (req: any, res: any, next: any) => {
    try {
        userModel.findById(req.params.id, (err: any, user: any) => {
            if (err) { throw new Internal(err.message) } else { res.status(200).send(user) }
        })
    } catch (err) { next(err) }
})

authRouter.route('/:id').post(checkAuth, (req: any, res: any, next: any) => {
    try {
        userModel.findByIdAndUpdate(req.params.id, req.body, { runValidators: true },
            err => {
                if (err) { throw new Internal(err.message) } else { res.status(200).send('Usuario modificado con exito!') }
            })
    } catch (err) { next(err) }
})

authRouter.route('/access/logout').post(checkAuth, async (req: any, res: any, next: any) => {
    try {
        req.user.tokens = req.user.tokens.filter((token: any) => req.token != token.token)
        await req.user.save((err: any) => {
            if (err) { throw new Internal(err.message) } else { res.status(200).send('User logged out successfully!') }
        })
    } catch (err) {
        next(err)
    }
})
export default authRouter;