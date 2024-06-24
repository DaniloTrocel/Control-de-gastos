const conexion = require('../conexion')

const todos = (req, res)=>{
    const sql = 'SELECT * FROM movimiento'
    conexion.query(sql, (err, result)=>{
        if (err){
            res.send('Ha ocurrido un error'+ err)
        }else{
            res.send(result)
        }
    })
}

const buscar = (req, res) => {
    const id = req.params.id;
    const sql = `SELECT * FROM movimiento WHERE id=${id}`;
    conexion.query(sql, (err, result) => {
        if (err) {
            res.status(500).send({ error: 'Ha ocurrido un error' + err });
        } else {
            if (result.length > 0) {
                res.status(200).json(result[0]); // Asegúrate de enviar un JSON válido
            } else {
                res.status(404).send({ error: 'Movimiento no encontrado' });
            }
        }
    });
};


const registrar = (req, res)=>{
    const sql = 'INSERT INTO movimiento set ?'
    conexion.query(sql, req.body, (err)=>{
        if (err){
            res.send('Ha ocurrido un error' + err)
        }else{
            res.send('Registro correcto')
        }
    })
}

const modificar = (req, res) => {
    const id = req.params.id;
    const campo = req.body.campo;
    const nuevo_valor = req.body.nuevo_valor;
    const sql = `UPDATE movimiento SET ${campo}='${nuevo_valor}' WHERE id=${id}`;
    conexion.query(sql, (err) => {
        if (err) {
            res.status(500).send('Ha ocurrido un error' + err);
        } else {
            res.send('Se ha actualizado correctamente');
        }
    });
};


const eliminar = (req, res) =>{
    const id = req.params.id
    const sql = `DELETE FROM movimiento WHERE id=${id}`
    conexion.query(sql, (err)=>{
        if (err){
            res.send('Ha ocurrido un error'+ err)
        }else{
            res.send('Se ha eliminado correctamente')
        }
    })
}

module.exports = {
    todos, buscar, registrar, modificar, eliminar
}