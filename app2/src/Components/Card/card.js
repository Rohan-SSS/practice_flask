import React from 'react'

const Card = ({listOfTodos}) => {
  return (
    <>
        {listOfTodos.map(todo => {
            return (
                <ul key = {todo.id}>
                    <li >
                        {todo.content}
                    </li>
                </ul>
            )
        })}
    </>
  )
}

export default Card