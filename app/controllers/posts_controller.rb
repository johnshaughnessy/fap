class PostsController < ApplicationController
  def show
    @post = Post.find_by_id(params[:id])
    @similar_posts = Post.for_category(@post.category)
  end

  def new
    @post = Post.create
  end

  def create
    @post = Post.create(params[:post])
    @post.published = true

    if @post.save
      redirect_to post_path(@post.id), :notice => "Your post has been created"
    else
      render "new"
    end
  end

  def edit
    @post = Post.find(params[:id])
  end

  def update
    @post = Post.find(params[:id])
    if @post.update_attributes(params[:post])
      redirect_to post_path
    else
      render "edit"
    end
  end
end
