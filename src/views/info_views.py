from datetime import datetime

from flask import Blueprint, render_template, request, url_for, flash, session, g
# from werkzeug.utils import redirect
# from sqlalchemy import func

from .. import db
from ..models import User, Vac

bp = Blueprint('userinfo', __name__, url_prefix='/userinfo')

@bp.route('/infolist/')
def infolist():
    user_id = session.get('user_id')
    # 입력 파라미터
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')

    # info_list = Vac.query.order_by(Vac.create_date.desc())
    info_list = Vac.query.filter_by(id=user_id)

    # 페이징
    info_list = info_list.paginate(page, per_page=10)
    return render_template('userinfo/info.html', info_list=info_list, page=page, kw=kw)


