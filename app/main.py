from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference


app = FastAPI()

shipments = {
    12701: {
        "weight": 2.2,
        "content": "glassware",
        "status": "placed"
    },
    12702: {
        "weight": 1.5,
        "content": "books",
        "status": "in transit"
    },
    12703: {
        "weight": 3.8,
        "content": "electronics",
        "status": "delivered"
    },
    12704: {
        "weight": 0.9,
        "content": "clothing",
        "status": "placed"
    },
    12705: {
        "weight": 5.1,
        "content": "furniture",
        "status": "in transit"
    },
    12706: {
        "weight": 0.5,
        "content": "documents",
        "status": "delivered"
    },
    12707: {
        "weight": 4.3,
        "content": "kitchen appliances",
        "status": "placed"
    },
}


@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:

    if not id:
        id = max(shipments.keys())
        return shipments[id]

    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )

    return shipments[id]


@app.post("/shipment")
def submit_shipment(data: dict[str, Any]) -> dict[str, Any]:
    content = data["content"]
    weight = data["weight"]

    if weight > 25:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Shipment weight exceeds the maximum limit of 25 kg"
        )

    new_id = max(shipments.keys()) + 1

    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "status": "placed",
    }

    return {"id": new_id, "message": "Shipment submitted successfully"}


@app.get("/shipment/{field}")
def get_shipment_field(field: str, id: int) -> dict[str, Any]:
    return {
        field: shipments[id][field]
    }


@app.put("/shipment")
def shipment_update(id: int, content: str, weight: float, shipment_status: str) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )

    shipments[id] = {
        "content": content,
        "weight": weight,
        "status": shipment_status,
    }

    return shipments[id]


@app.patch("/shipment")
def patch_shipment(id: int, body: dict[str, Any]) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shipment not found"
        )

    shipments[id].update(body)

    return shipments[id]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API",
    )
